class __NoInitMeta(type):
	def __call__(cls, *_, **__):
		raise RuntimeError("This class doesnt support initialization, it is a scope/container for other values or (static/class)methods only.")


class Scope(metaclass=__NoInitMeta):  # inherit metaclass
	...
