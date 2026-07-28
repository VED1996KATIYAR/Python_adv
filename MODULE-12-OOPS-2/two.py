class A:
    def add(self, *args):
        return sum(args) # यह सभी पास किए गए नंबर्स को आपस में जोड़ देगा

obj = A()
print(obj.add(1, 2))          # आउटपुट: 3
print(obj.add(1, 2, 3))       # आउटपुट: 6
print(obj.add(1, 2, 3, 4))    # आउटपुट: 10
