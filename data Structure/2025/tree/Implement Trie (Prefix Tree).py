class Trie:

    def __init__(self):
        self.head = {}

    def insert(self, word: str) -> None:
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = True


    def search(self, word: str) -> bool:
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        if '*' in cur:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for ch in prefix:
            if ch not in cur:
                return False
            cur = cur[ch]
        return True

commands = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
args = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

output = []
trie = None

for cmd, arg in zip(commands, args):
    if cmd == "Trie":
        trie = Trie()
        output.append(None)  # null
    elif cmd == "insert":
        trie.insert(arg[0])
        output.append(None)  # null
    elif cmd == "search":
        output.append(trie.search(arg[0]))
    elif cmd == "startsWith":
        output.append(trie.startsWith(arg[0]))

print(output)