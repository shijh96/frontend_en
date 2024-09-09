#from phonemizer import phonemize
from phonemizer.backend import EspeakBackend
from tn.english.normalizer import Normalizer as EnNormalizer
import sys

class Normalizer:
    def __init__(self):
        self.en_tn_model = EnNormalizer(cache_dir = "/mnt/d/workspace/WeTextProcessing/tn")
    
    def normalize(self, text):
        return self.en_tn_model.normalize(text)
    
class Phonemizer:
    def __init__(self):
        self.backend = EspeakBackend('en-us')
        self.normalizer = Normalizer()

    def convert(self, text):

        if isinstance(text, list):
            text = [self.normalizer.normalize(x) for x in text]
            phonemes = self.backend.phonemize(text)
        else:
            text = self.normalizer.normalize(text)
            phonemes = self.backend.phonemize([text])
        return phonemes

    def convert_file(self, input_file, output_file='phonemizer_output.txt'):
        with open(input_file, 'r', encoding='utf-8') as f:
            sentences = [line.strip() for line in f if line.strip()]
        
        phonemes = self.convert(sentences)
        with open(output_file, 'w', encoding='utf-8') as f:
            for phoneme in phonemes:
                f.write(f"{phoneme}\n")
        print(f"转换结果已写入 {output_file}")

def main():
    phonemizer = Phonemizer()

    if len(sys.argv) < 2:
        print("用法: python test_frontend_en.py <输入文本或文件> [输出文件]")
        return

    input_text = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    if input_text.endswith('.txt'):
        if not output_file:
            output_file = input_text.replace('.txt', '_phonemes.txt')
        phonemizer.convert_file(input_text, output_file)
    else:
        phonemes = phonemizer.convert(input_text, None)
        for p in phonemes:
            print(p)

if __name__ == "__main__":
    main()

