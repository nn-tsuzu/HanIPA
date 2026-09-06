import re
from jamo import h2j, j2hcj
from g2pk2 import G2p

HANGUL = str.maketrans({
    # 子音
    "ㄱ":"g", "ㄲ":"kʼ", "ㅋ":"kʰ",
    "ㄷ":"d", "ㄸ":"tʼ", "ㅌ":"tʰ",
    "ㅂ":"b", "ㅃ":"pʼ", "ㅍ":"pʰ",
    "ㅅ":"sʰ", "ㅆ":"sʼ",
    "ㅈ":"d͡ʑ", "ㅊ":"t͡ɕʰ", "ㅉ":"t͡ɕʼ",
    "ㅁ":"m", "ㄴ":"n", "ㅇ":"ŋ",
    "ㄹ":"ɾ",
    "ㅎ":"h",
    # 二重子音
    "ㄳ":"ks",
    "ㅄ":"bs",
    "ㄵ":"nd͡ʑ", "ㄶ":"n",
    "ㄺ":"rk", "ㄻ":"rm", "ㄼ":"rb", "ㄽ":"rs", "ㄾ":"rt", "ㄿ":"rp", "ㅀ":"r",
    # 母音
    "ㅑ":"j͡a", "ㅕ":"j͡ʌ", "ㅠ":"j͡u", "ㅛ":"j͡o",
    "ㅐ":"ɛ", "ㅔ":"e", "ㅒ":"j͡ɛ̝", "ㅖ":"j͡e",
    "ㅏ":"a", "ㅗ":"o", "ㅓ":"ʌ",
    "ㅣ":"i",
    "ㅜ":"u", "ㅡ":"ɯ",
    # 二重母音
    "ㅘ":"w͡a", "ㅝ":"w͡ʌ",
    "ㅚ":"ø", "ㅞ":"w͡e", "ㅙ":"w͡ɛ",
    "ㅟ":"w͡i", "ㅢ":"ɰ͡i",
})
MOEUM = set([
    # 母音
    "ㅑ", "ㅕ", "ㅠ", "ㅛ",
    "ㅐ", "ㅔ", "ㅒ", "ㅖ",
    "ㅏ", "ㅗ", "ㅓ",
    "ㅣ",
    "ㅜ", "ㅡ",
    # 二重母音
    "ㅘ", "ㅝ",
    "ㅚ", "ㅞ", "ㅙ",
    "ㅟ", "ㅢ",
])
WORD_INITIAL_MAP = str.maketrans({"b":"b̥", "d":"d̥", "g":"k"})
MOEUM_STR = "".join(MOEUM)
RE_SILENT_IEUNG = re.compile(rf'ㅇ(?=[{MOEUM_STR}])') # for moeum
RE_LIQUID = re.compile(r"ɾ(?=[^aeiouʌɯ])|ɾ$") # for ㄹ

IPA_VOWELS = set('aeiouɛɜɪʊʌɯøɔɐæɑɒə')
PROLONGED_MARKS = set(['~', '〜', 'ー', '～', '-'])

_g2p = G2p()

def convert(text: str, g2p) -> tuple:
        # convert
        text = g2p(text, descriptive=True)
        # 모음 자음을 분리
        text = j2hcj(h2j(text))
        # 받침이 아닌 ㅇ을 지움
        text = RE_SILENT_IEUNG.sub('', text)
        # 한글 to IPA
        text = text.translate(HANGUL)

        # split
        text = re.sub(r'\s+', ' ', text)
        text = re.split(r'([,.!? ])', text)

        result = []

        for token in text:
            # 단어 머리 ㄱㅂㅈㄷ을 변환(g b d͡ʑ d -> k p t͡ɕ t)
            if token[:3] == "d͡ʑ":
                token = "t͡ɕ" + token[3:]
            elif token[:1] in "bdg":
                token = token[:1].translate(WORD_INITIAL_MAP) + token[1:]
            result.extend(token)

        result = "".join(result)

        # 어중의 ㄹ 발음을 ɾ -> l 
        result = RE_LIQUID.sub("l", result)
        result = expand_prolonged(result)
        return result


def expand_prolonged(text: str) -> str:
    result = []
    last_vowel = None
    
    for ch in text:
        if ch in PROLONGED_MARKS:
            if last_vowel:
                result.append(last_vowel)
        else:
            result.append(ch)
            if ch in IPA_VOWELS:
                last_vowel = ch
    return ''.join(result)


class G2P_Korean_to_Phoneme():
    def __init__(self):
        self.g2p = _g2p
    
    def __call__(self, text):
        return convert(text, self.g2p)


if __name__ == "__main__":
    h = G2P_Korean_to_Phoneme()
    a = h('한국인은 자주 김치를 먹어요.')
    print(a)