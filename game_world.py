objects = [[] for _ in range(4)]

# fill here
collision_pairs={} #{'boy:ball':[[boy],[ball,ball,....]]}
def add_object(o, depth = 0):
    objects[depth].append(o)

def add_objects(ol, depth = 0):
    objects[depth] += ol


def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
    for layer in objects:
        for o in layer:
            o.draw()

# fill here
def remove_collsion_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)
    pass

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o) #시각적 월드에서만 제거함
            remove_collsion_object(o) # 충돌 그룹에서 삭제 완료
            del o #쓸모없는 객체 자체를 제거
            return
    raise ValueError('Cannot delete non existing object')


def clear():
    for layer in objects:
        layer.clear()



# fill here
def collide(a,b):
    la,ba,ra,ta=a.get_bb()
    lb,bb,rb,tb=b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    return True

def add_collision_pair(group,a,b):
    if group not in collision_pairs:
        print(f'new group {group} added')
        collision_pairs[group]=[[],[]]
    if a: #a가 있을 때 -> a가 None이 아니면..
        collision_pairs[group][0].append(a)
    if b:
        collision_pairs[group][1].append(b)


def handle_collsions():
    #등록된 모든 충돌 상황에 대해 충돌 검사, 충돌 처리 수행
    for group,pairs in collision_pairs.items(): # key :string value : list of list
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a,b):
                    a.handle_collsion(group,b) #충돌 종류, 총돌 객체
                    b.handle_collsion(group,a)
    return None