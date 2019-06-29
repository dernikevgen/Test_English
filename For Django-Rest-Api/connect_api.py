import requests
import json


class ConnectDjangoApi:

    def value_list(self):
        '''
        Connect to server, choice values
        and return list.
        '''
        self.verbs_list = []
        s = requests.get("http://127.0.0.1:8000/api/articles/")
        data = s.json()
        data = data['articles']
        for i in data:
            for j in i:
                self.verbs_list.append(i[j])
        return self.verbs_list

    def count_input(self):
        '''
        Calculate probable quantity True/False input values
        '''
        max_flags = len(self.verbs_list) - (len(self.verbs_list) // 4)
        return max_flags

    def value_dict(self):
        '''
        Create dict based value_list 'return'
        '''
        lst = [i for i in range(1,len(self.verbs_list)+1)]
        verbs_dict = {i: i for i in range(1, len(lst) + 1)}
        j = 0
        for i in range(1, len(lst) + 1):
            verbs_dict[i] = self.verbs_list[j]
            j += 1
        return verbs_dict

