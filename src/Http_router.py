class RouteTrieNode:
    def __init__(self):
        self.children = {}
        self.handler = None
    def insert(self, path,handler=None):
        if path not in self.children:
            self.children[path] = RouteTrieNode(handler)
class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode()
        self.handler = None
    
    def insert(self, collection_of_paths, handler):
        node = self.root
        for path in collection_of_paths:
            if path not in node.children:
                node.children[path] = RouteTrieNode()
            node = node.children[path]
        node.handler = handler

    def find(self, collection_of_paths):
        node = self.root

        for path in collection_of_paths:
            if path not in node.children:
                return None
            node = node.children[path]

        return node.handler


class Router:
    def __init__(self, handler, not_found_handler="404"):
        self.routes = RouteTrie()
        self.routes.insert("/", handler)
        self.not_found = not_found_handler
    def add_handler(self, route, handler):
    
        paths = self.split_path(route)
        self.routes.insert(paths, handler)


    def lookup(self, route):
        paths = self.split_path(route)
        return self.routes.find(paths) or self.not_found
 
    def split_path(self, route):
        if len(route) != 1:
            return route.strip("/").split("/")
            
        else:
            return ["/"]
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print("'': ", router.lookup(""))  #'not found handler'
print("'/': ", router.lookup("/"))  #'root handler'
print("'/home/': ", router.lookup("/home"))  # 'not found handler'
print("'/home/about': ", router.lookup("/home/about"))  # 'about handler'
print("'/home/about/': ", router.lookup("/home/about/"))  # 'about handler'
print("'/home/about/me': ", router.lookup("/home/about/me"))  # 'not found handler'