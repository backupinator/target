'''Target class.'''

class Target:
    '''Implements the Target API.'''

    def __init__(self):
        # Every target needs a unique name
        self.target_name = 'temp'

    def collect_backups(self):
        '''Get all backups for the target.'''

    def send_manifest(self, client_name):
        '''Send a list of all client files currently on the target.'''

        print(client_name)

if __name__ == '__main__':

    target = Target()
