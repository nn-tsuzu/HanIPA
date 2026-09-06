# HanIPA
<img width="1025" height="205" alt="logo" src="https://github.com/user-attachments/assets/523ba934-a275-406c-ab32-5682f7476bec" />

간단한 규칙기반 한글 to ipa 변환기. TTS 등에 사용할 수 있습니다.

# Install

```
pip install git+https://github.com/nn-tsuzu/Hangul-to-IPA.git
```

# How to use
```
from Korean_to_IPA import G2P_Korean_to_Phoneme

g2p = G2P_Korean_to_Phoneme()
text = g2p('한국인은 자주 김치를 먹어요.')
print(text) # → hanguginɯn t͡ɕad͡ʑu kimt͡ɕʰiɾɯl mʌgʌj͡o.
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
