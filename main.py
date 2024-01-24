from typing import Union
import traceback
import datetime
import random
import time

class ProxyLimiter:
    def __init__(self, proxies: list[str], timeout: int = 30) -> None:
        self.proxies = proxies
        self.proxies_data = {}
        self.timeout = timeout

        for item in self.proxies:
            self.proxies_data[item] = None

    def get_proxy(self, no_limits: bool = False, any_if_timeout: bool = False) -> Union[str, None]:
        """
        no_limits: bool = False - Return a random proxy from list or listen to timeout.
        """
        
        if not self.proxies: # If there are no proxies in list - return None
            return None
        
        if no_limits == True:
            if self.proxies:
                return random.choice(self.proxies)
            else:
                return None
        else:
            for proxy, date in self.proxies_data.items():
                if date:
                    if (datetime.datetime.now() - date).seconds >= self.timeout:
                        return proxy
                else:
                    return proxy
            
            if any_if_timeout == True:
                return random.choice(self.proxies)
            else:
                return None
            
    def append_proxy(self, proxy: str) -> None:
        if proxy in self.proxies:
            return
        
        self.proxies.append(proxy)
        self.proxies_data[proxy] = None

    def remove_proxy(self, proxy: str) -> None:
        if proxy in self.proxies:
            try:
                self.proxies.remove(proxy)
            except:
                print(traceback.format_exc())
        if self.proxies_data.get(proxy):
            try:
                del self.proxies_data[proxy]
            except:
                print(traceback.format_exc())

        return
    
    def add_used_proxy(self, proxy: str, time: datetime.datetime = None) -> None:
        self.append_proxy(proxy)

        if proxy in self.proxies:
            if not time:
                self.proxies_data[proxy] = datetime.datetime.now()
            else:
                self.proxies_data[proxy] = time

        return

def main() -> None:
    """Simulation of a real worker."""
    
    proxies = ["1_proxy", "2_proxy", "3_proxy", "4_proxy", "5_proxy"] # A list of all proxies
    limiter = ProxyLimiter(proxies) # Initialize class with proxy list
    
    while True:
        proxy = limiter.get_proxy(any_if_timeout=True) # Getting a proxy for a request
        print(f"Making request with: {proxy}") # Making request with proxy
        limiter.add_used_proxy(proxy) # Telling that proxy was used

        time.sleep(0.1)

if __name__ == "__main__":
    main()