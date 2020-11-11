__version__="1.0.0.1"
from functools import reduce

import click 

class TaylorSeries:
    
    def exponential_function(self, value, count):
        return sum([float(value)**n/self.__factorial(n) for n in range(count)])

    def __factorial(self, value):
        return reduce((lambda x,y:x*y),list(range(1,value+1)), 1)


@click.group()
def main():
    pass

@main.command()
@click.option("--value", type=int, help="Value for function")
@click.option("--count", type=int, help="Count of steps for series.")
def run(value, count):
    if count<1:
        raise Exception("'count' must be more than 0.")
    taylor_series = TaylorSeries()
    result = taylor_series.exponential_function(value, count)
    print(f"Result: {result}")
    return result    


if __name__ == "__main__":
    main()