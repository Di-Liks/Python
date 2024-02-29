import re

task = int(input("Выберите номер задания от 1 до 3: "))
match task:
    case 1:
        file = open("dateNum.txt")
        s = file.readlines()
        n = int(s[0])
        max_ch = 0
        max_n = 0
        max_ch17 = 0
        max_n17 = 0
        for i in range(1, n + 1):
            s[i] = int(s[i])
            if s[i] % 2 == 0:
                if s[i] % 17 == 0 and s[i] > max_ch17:
                    max_ch17 = s[i]
                elif s[i] % 17 == 0 and s[i] <= max_ch17:
                    if s[i] > max_ch:
                        max_ch = s[i]
                elif s[i] > max_ch:
                    max_ch = s[i]
            elif s[i] % 2 != 0:
                if s[i] % 17 == 0 and s[i] > max_n17:
                    max_n17 = s[i]
                elif s[i] % 17 == 0 and s[i] <= max_n17:
                    if s[i] > max_n:
                        max_n = s[i]
                elif s[i] > max_n:
                    max_n = s[i]
        if max_n17 + max_n == 0 and max_ch17 + max_ch == 0:
            print(0, 0)
        elif max_n17 + max_n > max_ch17 + max_ch:
            print(max_n17, max_n)
        else:
            print(max_ch17, max_ch)
    case 2:
        filename = 'DateText.txt'
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

            sentences = re.split(r'(?<=[.!?])\s+', text)

            words_in_sentences = [re.findall(r'\b\w+\b', sentence) for sentence in sentences]

            common_word = set(words_in_sentences[0])

            for words in words_in_sentences[1:]:
                common_word.intersection_update(words)

            if common_word:
                print(f"Общее слово в каждом предложении: {common_word.pop()}")
            else:
                print("В каждом предложении нет общего слова.")
    case 3:
        with open('DateVideo.txt', 'r') as file:
            n, k = map(int, file.readline().split())
            durations = list(map(int, file.readline().split()))

        total_duration = sum(durations)

        if total_duration % k != 0:
            print("Нет")
        else:
            post_duration = total_duration // k
            post_videos = []
            current_duration = 0
            current_post = []

            for i in range(n):
                current_duration += durations[i]
                current_post.append(i + 1)

                if current_duration == post_duration:
                    post_videos.append(current_post)
                    current_duration = 0
                    current_post = []
                elif current_duration > post_duration:
                    print("Нет")
                    break

            else:
                if current_duration != 0:
                    print("Нет")
                else:
                    print("Да")
                    for post in post_videos:
                        print(len(post), end=" ")

#6 3
#3 3 1 4 1 6

#3 3
#1 1 1

#3 3
#1 1 2

#3 1
#1 10 100
