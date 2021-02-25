import math

class Time:
    """Egyszeru osztaly eltelt ido modellezesere
    """

    def __init__(self, seconds:int=0):
        self.time = seconds
        """Inicializalja az idot a megadott masodpercekkel

        Args:
            seconds (int): a masodpercek szama
        """
        
    def to_seconds(self, time:int):
        return time
        """Adja vissza egy `int`-ben, hogy masodpercben kifejezve mennyi az ido

        Returns:
            int: a tarolt ido masodpercekben

        >>> Time(12).to_seconds()
        12
        >>> Time(345).to_seconds()
        345
        """

    def _ss(self, time:int):
        ss = time % 60
        return ss
        """Visszaadja, hogy mennyit mutat a "masodpercmutato"

        Returns:
            int: egesz perceket leszamitva a masodpercek szama

        >>> Time(12)._ss()
        12
        >>> Time(72)._ss()
        12
        >>> Time(1234)._ss()
        34
        """
    
    def _mm(self, time:int):
        mm = math.floor ((time % 3600)/60)
        return mm
        """Visszaadja, hogy mennyit mutat a "percmutato"

        Returns:
            int: egesz orakat leszamitva az egesz percek szma

        >>> Time(12)._mm()
        0
        >>> Time(72)._mm()
        1
        >>> Time(1234)._mm()
        20
        """
    
    def _hh(self, time:int):
        hh = math.floor (time / 3600)
        return math.floor(hh)
        """Visszaadja, hogy mennyit mutat az "oramutato", amely sosem nullazodik.

        Returns:
            int: az egesz letelt orak szama, 24 fole is mehet
        
        >>> Time(12)._hh()
        0
        >>> Time(72)._hh()
        0
        >>> Time(1234)._hh()
        0
        >>> Time(3600)._hh()
        1
        >>> Time(12345)._hh()
        3
        """
    
    def pretty_format(self, time:int):
        if time < 60:
            pretty_time = str(time % 60)
            return pretty_time
        elif time >= 60 and time < 3600:
            pretty_time = str("{}:{}".format(f"{math.floor (time / 60):02d}", f"{time % 60:02d}"))
            return pretty_time
        else:
            pretty_time = str("{}:{}:{}".format(math.floor (time / 3600), f"{math.floor ((time % 3600)/60):02d}", f"{time % 60:02d}"))
            return pretty_time
        """Visszaadja az idot szep modon
         - `s` vagy `ss` egy perc alatt
         - `m:ss` vagy `mm:ss` egy perc felett es egy ora alatt
         - `h:mm:ss` egy ora felett. (Az orak szama tetszolegesen nagy lehet)

        Returns:
            str: a szepen formazott ido

        >>> Time(12).pretty_format()
        '12'
        >>> Time(72).pretty_format()
        '1:12'
        >>> Time(3600).pretty_format()
        '1:00:00'
        >>> Time(12345).pretty_format()
        '3:25:45'
        >>> Time(123456).pretty_format()
        '34:17:36'
        """



    def set_from_string(self, time:str):
        ss = "0"
        mm = "0"
        hh = "0"
        s = len(time)
        e = len(time)
        c = 0
        while s >= 0:
            if (time[s-1] == ":" and c==0) or ((s) == 0 and c ==0):
                ss = time[s:e]
                c+=1
                e = s-1
            elif (time[s-1] == ":" and c==1) or ((s) == 0 and c ==1):
                mm = time[s:e]
                c+=1
                e = s-1
            elif (time[s-1] == ":" and c==2) or ((s-1) == 0 and c ==2):
                hh = time[s-1:e]
            s-=1 
        ugly_time = int(hh)*3600 + int(mm)*60 + int(ss)
        return ugly_time

        """Beallitja az idot egy string alapjan, melynek a formatuma olyan mint a `pretty_format` eseteben.

        Returns:
            int: a beallitott ido masodpercekben

        Args:
            time (str): az ido szoveg formaban
        
        >>> Time().set_from_string('12')
        12
        >>> Time().set_from_string('1:12')
        72
        >>> Time().set_from_string('1:00:00')
        3600
        >>> Time().set_from_string('3:25:45')
        12345
        >>> Time().set_from_string('111:01:23')
        399683
        """
