class CWMeta(type):
    def __new__(cls, clsname, basecls, clsdict):
        print("In new")
        print(clsdict)
        print(cls)
        return super().__new__(cls, clsname, basecls, clsdict)

obj = CWMeta("CWMeta", (), {})
print(type(CWMeta))
