import cProfile, pstats, io
from pstats import SortKey


class Profile:
    def __init__(self):
        pass

    def __enter__(self):
        self.pr = cProfile.Profile()
        self.pr.enable()

    def __exit__(self, *exc):
        self.pr.disable()
        s = io.StringIO()
        sortby = SortKey.TIME
        ps = pstats.Stats(self.pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())