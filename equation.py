def eqSphere(keyword):
    radius = keyword.get('radius')
    pos = [radius,radius,radius]
    return ((keyword.get('x')-pos[0])**2)+((keyword.get('y')-pos[1])**2)+((keyword.get('z')-pos[2])**2) <= keyword.get('radius')

def eqStick(keyword):
    Length = keyword.get('Length')
    Width = keyword.get('Width')
    Height = keyword.get('Height')
    position = keyword.get('position',[0,0,0])
    x = keyword.get('x')
    y = keyword.get('y')
    z = keyword.get('z')
    return (position[0]<=x<position[0]+Length and position[1]<=y<position[1]+Width and position[2]<=z<position[2]+Height)

    
