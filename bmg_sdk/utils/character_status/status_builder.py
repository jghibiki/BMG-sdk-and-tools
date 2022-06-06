from importlib import resources

from moviepy.editor import *
import moviepy.video.fx.all as vfx
from thefuzz import fuzz, process

from bmg_sdk.compendium.compendium_loader import CompendiumLoader
from bmg_sdk.utils.character_status import assets
from bmg_sdk.utils.common import get_sanitized_name, Paths
from bmg_sdk.utils.scraper.util import character_card_paths


class StatusBuilder:
    stun_img = None
    blood_img = None
    bg_key_color = (0, 255, 0)

    def __init__(self, character: str, config):
        self.character_name = character
        self._character = None
        self.config = config
        self.compendium = CompendiumLoader().load()

    @property
    def character(self):
        if self._character is None:
            characters = {c.alias: c for c in self.compendium.characters.all}
            just_names = list(characters.keys())
            match = process.extractOne(
                self.character_name,
                just_names
            )

            self._character = characters[match[0]]
        return self._character

    def _load_stun_img(self):
        if StatusBuilder.stun_img is None:
            StatusBuilder.stun_img = resources.path(assets, "stun.png")

    def _load_blood_img(self):
        if StatusBuilder.blood_img is None:
            StatusBuilder.blood_img = resources.path(assets, "blood.png")

    def _build_stun_indicators(self, stun):
        stun_text_clip = (
            TextClip(
                txt=str(stun),
                color="red",
                fontsize=34
            )
                .set_duration(0.5)
                .set_position((545, 128))
        )

        self._load_stun_img()
        stun_img_clip = (
            ImageClip(str(StatusBuilder.stun_img), duration=0.5)
                .fx(vfx.resize, newsize=0.35)
                .set_position((560, 128))
        )
        return stun_text_clip, stun_img_clip

    def _build_blood_indicators(self, blood):
        blood_text_clip = (
            TextClip(
                txt=str(blood),
                color="red",
                fontsize=34
            )
                .set_duration(0.5)
                .set_position((665, 128))
        )

        # load icons
        self._load_blood_img()
        blood_img_clip = (
            ImageClip(str(StatusBuilder.blood_img), duration=0.5)
                .fx(vfx.resize, newsize=0.35)
                .set_position((680, 128))
        )

        return blood_text_clip, blood_img_clip

    def _blood(self, round:int ):
        return self.config[round].get("blood", 0)

    def _stun(self, round:int ):
        return self.config[round].get("stun", 0)

    def _build_blood_and_stun_clips(self, round):
        blood_stun_layers = []
        blood = self._blood(round)
        stun = self._stun(round)
        if blood > 0:
            blood_text_clip, blood_img_clip = self._build_blood_indicators(blood)
            blood_stun_layers.append(blood_text_clip)
            blood_stun_layers.append(blood_img_clip)

        if stun > 0:
            stun_text_clip, stun_img_clip = self._build_stun_indicators(stun)
            blood_stun_layers.append(stun_text_clip)
            blood_stun_layers.append(stun_img_clip)

        return blood_stun_layers

    def _build_status_layers(self, round):

        return [] # TODO


    def _build_round_status(self, round: int):
        (image_path, _) = character_card_paths(self.character)
        card_clip = ImageClip(str(image_path), duration=0.5)

        blood_stun_layers = self._build_blood_and_stun_clips(round)
        status_layers = self._build_status_layers(round)

        card_with_stats_clip = CompositeVideoClip([
            card_clip,
            *blood_stun_layers,
            *status_layers
        ])

        card_fade_in_clip = card_with_stats_clip.fx(
            vfx.fadein,
            duration=0.5,
            initial_color=StatusBuilder.bg_key_color
        )

        card_size = card_fade_in_clip.size
        bg_size = (card_size[0] * 2, card_size[1])
        bg_clip = ColorClip(bg_size, duration=0.5, color=StatusBuilder.bg_key_color)

        # build composite clip
        zoom_in_clip = (
            CompositeVideoClip([
                bg_clip,
                card_fade_in_clip.set_position((card_size[0], 0))
            ]).fx(vfx.scroll, w=card_size[0], h=card_size[1], x_start=0, x_speed=bg_size[0])
        )

        zoom_out_clip = zoom_in_clip.fx(vfx.time_mirror)

        full_clip = concatenate_videoclips([
            zoom_in_clip,
            card_with_stats_clip.fx(vfx.accel_decel, new_duration=5),
            zoom_out_clip
        ])

        return full_clip

    def build(self):
        name = get_sanitized_name(self.character)

        for round in self.config.keys():
            clip = self._build_round_status(round)
            path = Paths.card_info_output / f"{name}_round_{round}.mp4"
            clip.write_videofile(str(path), fps=30, audio=False)

