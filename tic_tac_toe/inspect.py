from inspect import getsource, isfunction, ismethod
from gameparts import Board 

game = Board

print('='*20, 'Способ 1', '='*20)
print(type(game))
print(type(game) == Board)  # noqa: E721
print(type(game) is Board)
print(type(game)) == str  # noqa: E721

print(isinstance(game, Board))
print(isinstance(game, str))


print('='*20, 'Способ 2', '='*20)
print(game.__calss__)


print('='*20, 'Способ 3', '='*20)
print(dir(game))
print('__str__' in dir(game))
print(hasattr(game, '__str__'))


print('='*20, 'Способ 4', '='*20)
print(game.__class__.__dict__)


print('='*20, 'Способ 5', '='*20)
print(getsource(Board))
print(isfunction(game.display))
print(ismethod(game.display))

