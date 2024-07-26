from persistencia.persistencia import UsuarioP
if __name__ == '__main__':
    
    p = UsuarioP()
    print(p.usuarios[0].to_dict())