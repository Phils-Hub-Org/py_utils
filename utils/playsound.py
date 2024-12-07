# # utils/playsound.py

"""
[Approach 2]
This approach is designed for rapid playback
"""

import pygame

class PlaySound:
    _sounds = {}

    @classmethod
    def preload_sounds(cls, sound_files: dict) -> None:
        """
        Preload sounds using PyGame's mixer to minimize latency.
        
        Args:
            sound_files (dict): A dictionary of sound types and file paths.
        """
        pygame.mixer.init()  # Initialize the mixer
        for sound_type, file_path in sound_files.items():
            if sound_type not in cls._sounds:
                cls._sounds[sound_type] = pygame.mixer.Sound(file_path)

    @classmethod
    def play_sound(cls, sound_type: str) -> None:
        """
        Play a preloaded sound effect.
        
        Args:
            sound_type (str): The type of sound to play.
        """
        if sound_type in cls._sounds:
            cls._sounds[sound_type].play()
    
    @classmethod
    def stop_sound(cls, sound_type: str) -> None:
        if sound_type in cls._sounds:
            cls._sounds[sound_type].stop()
    
    @classmethod
    def set_volume(cls, volume: float) -> None:
        """
        Set the volume for all loaded sounds.
        
        Args:
            volume (float): Volume level between 0.0 and 1.0
        """
        for sound in PlaySound._sounds.values():
            sound.set_volume(volume)

def preloadSounds(sound_files: dict) -> None:
    PlaySound.preload_sounds(sound_files)

def playSound(sound_type: str) -> None:
    PlaySound.play_sound(sound_type)

def stopSound(sound_type: str) -> None:
    PlaySound.stop_sound(sound_type)

def setVolume(volume: float) -> None:
    PlaySound.set_volume(volume)

if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)

    file_path = r'C:\Users\Phil-\OneDrive\__Workbase_Backup__\Resources\Envato\Sounds\Mountain Audio - Menu Click.wav'
    preloadSounds({'click': file_path})

    playSound('click')
    
    sys.exit(app.exec())