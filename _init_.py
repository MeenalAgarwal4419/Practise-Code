class URL:
    # suppose, we already have 10 billion urls
    id = 10000000000000000
    # store url to id in order not to have duplicated url with different id
    url2id = {}
    
    def short(self, original_url):
        if original_url in self.url2id:
            id = self.url2id[original_url]
            shorten_url = self.encode(id)
        else:
            # store url2id in order not to have duplicated url with different id in the future
            self.url2id[original_url] = self.id
            shorten_url = self.encode(self.id)
            # increase cnt for next url
            self.id += 1
    
        st=input("enter any string you want to add before the shorten url:")
        
        
            
            
        return st+shorten_url
    
    def encode(self, id):
        # base 70 characters
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"
        base = len(characters)
        ret = []
        # convert base10 id into base70 id for having alphanumeric shorten url
        while id > 0:
            val = id % base
            ret.append(characters[val])
            id = id // base
        # since ret has reversed order of base70 id, reverse ret before return it
        return "".join(ret[::-1])



