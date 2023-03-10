import wrap, random

wrap.world.create_world(800, 800)
wrap.world.set_back_color(255, 255, 255)
wrap.add_sprite_dir("sprite")
water = wrap.sprite.add("aqua", 400, 550, "water")
corm1 = wrap.sprite.add("aqua", 500, 200, "fishfood")
corm2 = wrap.sprite.add('aqua', 580, 200, "fishfood2")
fish = []
food = []
pf = None


@wrap.on_key_down(wrap.K_SPACE)
def poyavlenie():
    a = wrap.sprite.add("fish", 100, 700, random.choice(
        ["fish purple1", "fish pink1", "fish blue1", "fish colored1", "fish colored2", "fish colored3"]))
    riba = {"id": a, "skorostx": random.randint(2, 5), "skorosty": random.randint(2, 5)}
    fish.append(riba)
    print(fish)


def food1():
    ffood = wrap.sprite.add("aqua", wrap.sprite.get_x(corm1), wrap.sprite.get_bottom(corm1) + 10, "fish food granula")
    wrap.sprite.set_size(ffood, 11, 10)
    speed = random.randint(1, 2)
    sitnost = random.randint(2, 4)
    fff = {"id": ffood, "speed": speed, "sitnost": sitnost}
    food.append(fff)

    ffood = wrap.sprite.add("aqua", wrap.sprite.get_x(corm1) + 3, wrap.sprite.get_bottom(corm1) + 10,
                            "fish food granula")
    wrap.sprite.set_size(ffood, 11, 10)
    speed = random.randint(1, 2)
    sitnost = random.randint(2, 4)
    fff = {"id": ffood, "speed": speed, "sitnost": sitnost}
    food.append(fff)

    ffood = wrap.sprite.add("aqua", wrap.sprite.get_x(corm1) + 5, wrap.sprite.get_bottom(corm1) + 10,
                            "fish food granula")
    wrap.sprite.set_size(ffood, 11, 10)
    speed = random.randint(1, 2)
    sitnost = random.randint(2, 4)
    fff = {"id": ffood, "speed": speed, "sitnost": sitnost}
    food.append(fff)

    ffood = wrap.sprite.add("aqua", wrap.sprite.get_x(corm1) - 3, wrap.sprite.get_bottom(corm1) + 10,
                            "fish food granula")
    wrap.sprite.set_size(ffood, 11, 10)
    speed = random.randint(1, 2)
    sitnost = random.randint(2, 4)
    fff = {"id": ffood, "speed": speed, "sitnost": sitnost}
    food.append(fff)

    ffood = wrap.sprite.add("aqua", wrap.sprite.get_x(corm1) - 5, wrap.sprite.get_bottom(corm1) + 10,
                            "fish food granula")
    wrap.sprite.set_size(ffood, 11, 10)
    speed = random.randint(1, 2)
    sitnost = random.randint(2, 4)
    fff = {"id": ffood, "speed": speed, "sitnost": sitnost}
    food.append(fff)


@wrap.on_mouse_down(wrap.BUTTON_RIGHT)
def fishfood(pos_x, pos_y):
    global pf
    if pf == None:
        if wrap.sprite.is_collide_point(corm1, pos_x, pos_y):
            pf = corm1
        if wrap.sprite.is_collide_point(corm2, pos_x, pos_y):
            pf = corm2
        return
    wrap.sprite.set_angle(pf, 345)
    if pf == corm1:
        food1()


@wrap.on_mouse_up(wrap.BUTTON_RIGHT)
def ugol():
    if pf != None:
        wrap.sprite.set_angle(pf, 90)
        if wrap.sprite.get_bottom(pf) > wrap.sprite.get_top(water):
            wrap.sprite.move_bottom_to(pf, wrap.sprite.get_top(water))


@wrap.on_key_down(wrap.K_ESCAPE)
def otpuskanie():
    global pf
    if pf != None:
        if pf == corm1:
            wrap.sprite.move_to(pf, 500, 200)
        if pf == corm2:
            wrap.sprite.move_to(pf, 580, 200)
        wrap.sprite.set_angle(pf, 90)
        pf = None


@wrap.always()
def move_food():
    for f in food:
        wrap.sprite.move(f["id"], 0, f["speed"])


@wrap.on_mouse_move()
def peretaskivanie(pos_x, pos_y):
    if pf != None:
        wrap.sprite.move_to(pf, pos_x, pos_y)
        if wrap.sprite.get_bottom(pf) > wrap.sprite.get_top(water):
            wrap.sprite.move_bottom_to(pf, wrap.sprite.get_top(water))


@wrap.always(45)
def move():
    for f in fish:
        for v in food:
            x = wrap.sprite.get_x(v["id"])
            y = wrap.sprite.get_y(v["id"])
            s = f["skorostx"] + f["skorosty"]
            wrap.sprite.move_at_angle_point(f["id"], x, y, s/4)
            if wrap.sprite.get_right(f["id"]) >= 800 or wrap.sprite.get_left(f["id"]) <= 0:
                f["skorostx"] = -f["skorostx"]
                x = wrap.sprite.get_x(f["id"])
                y = wrap.sprite.get_y(f["id"])
                wrap.sprite.set_reverse_x(f["id"], not wrap.sprite.get_reverse_x(f["id"]))
                wrap.sprite.set_angle_to_point(f["id"], x + f["skorostx"], y + f["skorosty"])
            if wrap.sprite.get_bottom(f["id"]) >= 800:
                f["skorosty"] = -f["skorosty"]
                x = wrap.sprite.get_x(f["id"])
                y = wrap.sprite.get_y(f["id"])
                wrap.sprite.set_angle_to_point(f["id"], x + f["skorostx"], y + f["skorosty"])
                wrap.sprite.move_bottom_to(f["id"], 800)
            if wrap.sprite.get_top(f["id"]) <= wrap.sprite.get_top(water) - 10:
                f["skorosty"] = -f["skorosty"]
                x = wrap.sprite.get_x(f["id"])
                y = wrap.sprite.get_y(f["id"])
                wrap.sprite.set_angle_to_point(f["id"], x + f["skorostx"], y + f["skorosty"])
                wrap.sprite.move_top_to(f["id"], wrap.sprite.get_top(water) - 10)
            if wrap.sprite.is_collide_sprite(f["id"], v["id"]):
                wrap.sprite.remove(v["id"])
                shirina = wrap.sprite.get_width(f["id"])
                visota = wrap.sprite.get_height(f["id"])
                wrap.sprite.set_size(f["id"], shirina + v["sitnost"], visota + v["sitnost"])
                food.remove(v)


# v = []
# p1 = {"NAME":"ARTEM","AGE":10,"KG":40}
# p2 = {"NAME":"KIRILL","AGE":9,"KG":32}
# p3 = {"NAME":"SASHA","AGE":10,"KG":38}
# v.append(p1)
# v.append(p2)
# v.append(p3)
# #del p1,p2,p3
# #p1[KG + 1]
# print(p1["KG"])
# p1["KG"] += 1
# p1["NOMER"] = 2
# for q in [10,20,30]:
#     print(q)
# for p in v:
#  p["AGE"] += 1
# r = 30
# for q in v:
#     q["YEARS"] = 2023-q["AGE"]
import wrap_py

wrap_py.app.start()
