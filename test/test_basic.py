import urtask
from urtask import UrTask


def test_basic1():

    class MyTask( UrTask ):
        pass

    task = MyTask()
