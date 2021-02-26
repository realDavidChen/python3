# Making Text-To-Speech fun with Python and gTTS

https://www.youtube.com/watch?v=tIFEe0W0BEA


https://pypi.org/project/gTTS/

### 1. basic sample, read text and play it

```

from gtts import gTTS
from playsound import playsound

tts = gTTS('this is the example by using gTTS')


tts.save('hello.mp3')
playsound('hello.mp3')

```

```
import os
from gtts import gTTS

text_to_read = "this is a test using gTTS, a python package library改变几个字，中英文混合朗读"
language = 'zh-cn'
slow_audio_speed = False

filename = "my_file.mp3"

"""
    Reading from a string
"""


def reading_from_string():
    audio_created = gTTS(text=text_to_read, lang=language)
    #  slow=slow_audio_speed
    audio_created.save(filename)

    os.system(f'start {filename}')


if __name__ == "__main__":
    reading_from_string()


```


