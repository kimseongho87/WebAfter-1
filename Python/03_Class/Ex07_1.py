class Score:
      def __init__(self, scores):
            self.scores=scores
            print(type(self.scores))
      
      def getTotal(self):
           return sum(self.scores)
      
      def getAverage(self):
           return sum(self.scores) / len(self.scores)

if __name__ == "__main__": 
    arr=[80, 90, 85, 75, 95]
    s=Score(arr)
    print(s.getTotal())
    print(s.getAverage())

    # 10분 시작합니다.
