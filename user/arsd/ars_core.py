class ARSKernel:
    def __init__(self):
        self.prev = 0
        self.curr = 1
        self.history = []

    def adapt(self, context=0):
        nxt = self.curr + (self.curr - self.prev) + context
        self.prev, self.curr = self.curr, nxt
        self.history.append(nxt)
        return nxt

    def run_steps(self, steps=10, context_fn=None):
        results = []
        for i in range(steps):
            ctx = context_fn(i) if context_fn else 0
            results.append(self.adapt(ctx))
        return results