class StockSpanner:
    def __init__(self):
        # Create stack to store data in format (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        
        # While price in stack is <= current price increase the span value
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            # Remove the tuple from stack
            self.stack.pop()
        
        # Update the stack with current price and span
        self.stack.append((price, span))
        
        return span