# Hangul-to-IPA
한글을 IPA로 변환합니다. TTS 등에 사용할 수 있습니다.

# Install
1. Clone this repository
```
git clone https://github.com/nn-tsuzu/Hangul-to-IPA.git
cd Hangul-to-IPA
```
2. Install python requirements
```
pip install -r requirements.txt
```

# How to use
```
from Korean_to_IPA import G2P_Korean_to_Phoneme

g2p = G2P_Korean_to_Phoneme()
text = g2p('사랑해~')
print(text) # → sʰaɾaŋhɛɛ
```

# Output
느낌표는 그대로
```
text = g2p('사랑해!!?')
# → sʰaɾaŋhɛ!!?
```
장음(長音)는 모음을 겹칩니다
```
text = g2p('사랑해~')
# → sʰaɾaŋhɛɛ
```
