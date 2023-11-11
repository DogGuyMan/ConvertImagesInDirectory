# ConvertImagesInDirectory

## 개요
1. 특정 디렉토리에 들어간 "A 이미지 형식"을 다른 "B 이미지 형식"으로 </br>
".A -> .B" 저장하는것을 자동화 시키는 간단한 프로그램.
2. 입력될 인자들은 다음과 같다.

```txt
directoryPath : 디렉토리 경로 (절대경로로 입력)
recursiveType : 선택한 디렉토리 내부의 하부 폴더에 들어간 이미지 들도 끝까지 변환 시킬것인지 유무를 Y/N로 결정
targetExtentionType : 변환시킬 이미지 형식 .A 입력
resultExtentionType : 결과 이미지 형식 .B를 입력
```

## 사용 예시
Terminal, Iterm과 같은 콘솔에서 실행

```shell
> python3 ImageConverter.py
경로를 String으로 입력해주세요 : 
"[어떤경로]"                        
현재 폴더에서만 실행(N), 내부 폴더까지 순회해서 실행(Y) : 
Y
변환할 이미지 형식을 입력해주세요 : 
jfif
변환될 결과 이미지 형식을 입력해주세요 : 
jpg
```

## 사용 모듈
1. os : 경로를 다루는데 사용
2. glob : 재귀적인 폴더 순회를 위해 사용
3. time : time.sleep을 위해 사용
4. tqdm  : 진행도 (Progress Bar)
5. pillow : 이미지 다루기
