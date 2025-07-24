# # import pyperclip
# # import keyboard
# # import pyautogui
# # import time
# # import traceback
# # from original import *
# # from win10toast import ToastNotifier

# # notifier = ToastNotifier()

# # def on_hotkey():
# #     try:
# #         # 1. 현재 선택된 텍스트 복사
# #         pyautogui.hotkey('ctrl', 'c')
# #         time.sleep(0.2)

# #         original = pyperclip.paste()
# #         if not original.strip():
# #             notifier.show_toast("SQL 정렬기", "⚠️ 복사된 텍스트가 없습니다.", duration=3)
# #             return

# #         # 2. SQL 정렬
# #         formatted = last_start(original)
# #         pyperclip.copy(formatted)

# #         # 3. 자동 붙여넣기
# #         time.sleep(0.2)
# #         pyautogui.hotkey('ctrl', 'v')

# #         notifier.show_toast("SQL 정렬기", "✅ 쿼리 정렬 완료!", duration=2)
# #     except Exception as e:
# #         error_msg = traceback.format_exc()
# #         notifier.show_toast("SQL 정렬기", "❌ 정렬 중 오류 발생", duration=5)
# #         # 오류 로그를 남기고 싶다면 아래 코드 활성화
# #         # with open("error_log.txt", "w", encoding="utf-8") as f:
# #         #     f.write(error_msg)

# # # 단축키 설정
# # keyboard.add_hotkey('ctrl+alt+q', on_hotkey)

# # # 프로그램 실행 유지
# # keyboard.wait()



# # import pyperclip
# # import keyboard
# # import pyautogui
# # import time
# # import traceback
# # from original import *
# # from win10toast import ToastNotifier
# # import threading

# # notifier = ToastNotifier()

# # def on_hotkey():
# #     def job():
# #         try:
# #             # 선택한 텍스트 복사
# #             pyautogui.hotkey('ctrl', 'c')
# #             time.sleep(0.3)  # 복사 대기시간 약간 여유

# #             original = pyperclip.paste()
# #             if not original.strip():
# #                 notifier.show_toast("SQL 정렬기", "⚠️ 복사된 텍스트가 없습니다.", duration=3)
# #                 return

# #             # SQL 정렬 처리
# #             formatted = last_start(original)
# #             pyperclip.copy(formatted)

# #             time.sleep(0.2)
# #             pyautogui.hotkey('ctrl', 'v')

# #             notifier.show_toast("SQL 정렬기", "✅ 쿼리 정렬 완료!", duration=2)

# #         except Exception:
# #             notifier.show_toast("SQL 정렬기", "❌ 오류 발생 (로그 확인)", duration=5)
# #             with open("error_log.txt", "w", encoding="utf-8") as f:
# #                 f.write(traceback.format_exc())

# #     # 🔁 쓰레드로 실행해야 반복 사용 가능
# #     threading.Thread(target=job).start()

# # # 단축키 등록
# # keyboard.add_hotkey('ctrl+alt+q', on_hotkey)

# # # 프로그램 유지
# ##keyboard.wait()


import os
import sys
import time

import pyperclip
import keyboard
import pyautogui
import time
import traceback
import threading
from original import *
from win10toast import ToastNotifier
import tkinter as tk
from tkinter import messagebox, scrolledtext
import re
from PyInstaller.utils.hooks import collect_data_files
import pkg_resources


notifier = ToastNotifier()

def show_diff_dialog(original: str, formatted: str) -> bool:


    # 공백과 줄바꿈 제거 후 문자 비교
    #original_chars = re.sub(r'\s+', '', original)
    original_chars = len( re.findall(r'[A-Za-z0-9\(\),\.\'\*=-]', original))
    
    #formatted_chars = re.sub(r'\s+', '', formatted)
    formatted_chars = len( re.findall(r'[A-Za-z0-9\(\),\.\'\*=-]', formatted))

    if original_chars == formatted_chars:
        return True  # 바뀐 문자가 없으면 자동 통과
#-----
    # UI 창 구성
    root = tk.Tk()
    root.title("SQL변경확인")

    # ✅ 창을 최상단으로 + 포커스 강제 설정
    root.attributes('-topmost', True)
    root.lift()
    root.focus_force()

    label = tk.Label(root, text="정렬된 결과가 원본과 다릅니다.\n내용을 확인한 후 적용 여부를 선택하세요.")
    label.pack(padx=10, pady=10)

    text_box = scrolledtext.ScrolledText(root, width=100, height=30, wrap=tk.WORD)
    text_box.insert(tk.END, formatted)
    text_box.configure(state='disabled')  # 읽기 전용
    text_box.pack(padx=10, pady=10)

    def on_yes():
        root.result = True
        root.destroy()

    def on_no():
        root.result = False
        root.destroy()

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="예 (적용)", width=12, command=on_yes).pack(side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="아니오 (취소)", width=12, command=on_no).pack(side=tk.LEFT, padx=10)

    root.result = False
    root.mainloop()
    return root.result


def on_hotkey():
    def job():
        try:
            # 1. 기존 내용 백업
            old_clip = pyperclip.paste()
            time.sleep(0.2)


            # 2. 텍스트 선택 상태에서 자동 복사
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(0.2)

            # 3. 복사 완료될 때까지 최대 1초 대기
            for _ in range(10):
                new_clip = pyperclip.paste()
                if new_clip != old_clip:
                    break
                time.sleep(0.1)

            if not new_clip.strip():
                notifier.show_toast("SQL 정렬기", "⚠️ 복사된 텍스트가 없습니다.", duration=3)
                return

            # 4. 정렬 처리
            formatted = last_start(new_clip)
            time.sleep(0.2)
            pyperclip.copy(formatted)

            # 변경 여부 확인
            if not show_diff_dialog(new_clip, formatted):
                notifier.show_toast("SQL 정렬기", "❌ 변경이 취소되었습니다.", duration=3)
                return

            # 5. 자동 붙여넣기
            time.sleep(0.2)
            pyautogui.hotkey('ctrl', 'v')

            notifier.show_toast("SQL 정렬기", "✅ 쿼리 정렬 완료!", duration=2)

        except Exception:
            notifier.show_toast("SQL 정렬기", "❌ 오류 발생 (로그 확인)", duration=5)
            # with open("error_log.txt", "w", encoding="utf-8") as f:
            #     f.write(traceback.format_exc())

    # 💡 쓰레드로 실행해야 반복 사용 가능
    threading.Thread(target=job).start()

# 프로그램 재시작 타이머 (600초 = 10분)
def restart_program(delay_seconds=600):
    def delayed_restart():
        time.sleep(delay_seconds)
        python = sys.executable
        os.execl(python, python, *sys.argv)  # 현재 프로세스를 새로 시작

    threading.Thread(target=delayed_restart, daemon=True).start()    

# 단축키 등록
keyboard.add_hotkey('ctrl+alt+q', on_hotkey)


# 재시작 예약
restart_program(600)  # 10분마다 재시작


# 프로그램 유지
keyboard.wait()


