class ThailandPackage:
    def detail(self):
        print("[태국 팻키지 3박 5일] 방콕,파타야 여행(야시장) 50만원")

if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행 할 때만 실행 돼요")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")