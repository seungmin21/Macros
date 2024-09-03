import pyautogui
import time
import keyboard

# 매크로 동작 함수
def run_macro(skill_key='q', jump_key='space', delay=5):
    try:
        while True:
            # 스킬 키 누르기
            pyautogui.press(skill_key)
            print(f"{skill_key} 키를 눌렀습니다.")

            # 짧은 지연
            time.sleep(0.1)

            # 점프 키 두 번 누르기
            pyautogui.press(jump_key)
            pyautogui.press(jump_key)
            print(f"{jump_key} 키를 두 번 눌렀습니다.")

            # 다음 매크로 실행까지 대기
            time.sleep(delay)
    except KeyboardInterrupt:
        print("매크로가 중지되었습니다.")

# 매크로 실행
if __name__ == "__main__":
    print("매크로를 시작하려면 's' 키를 누르고, 중지하려면 Ctrl+C를 누르세요.")
    
    keyboard.wait('s')  # 's' 키가 눌릴 때까지 대기
    run_macro()
