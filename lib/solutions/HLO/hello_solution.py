
class HelloSolution:
    
    # friend_name = unicode string
    def hello(self, friend_name:str)->str:
        #raise NotImplementedError()
        """
        Returns a greeting message for the given name.

        :param name: A string containing a name
        :return: A string containing a message
        """
        return f"Hello, {friend_name}!"
