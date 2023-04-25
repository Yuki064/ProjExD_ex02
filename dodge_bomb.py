import random
import sys
import pygame as pg

delta = {
    #keyの辞書
    pg.K_UP: (0, -1),
    pg.K_DOWN: (0, +1),
    pg.K_LEFT: (-1, 0),
    pg.K_RIGHT: (+1, 0)
}


def cheack_bound(scr_rct:pg.Rect, obj_rct:pg.Rect):
    """
    オブジェクトが画面内OR画面外を判定し　真理値タプルを返す
    引数１ :画面SarfaceのRect
    引数２ ：こうかとんか爆弾の
    戻り値 :横縦の判定結果
    """
    yoko, tate = True, True
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = False
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = False
    return yoko, tate



def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    tmr = 0

    bb_img = pg.Surface((20,20))
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)  # 爆弾作成
    bb_img.set_colorkey((0, 0, 0))
    x, y = random.randint(0,1600), random.randint(0,900)
    #screen.blit(bb_img, [x,y])
    vx,vy=+1,-1
    bb_rect = bb_img.get_rect()
    bb_rect.center = x, y
    kk_rect = kk_img.get_rect()
    kk_rect.center = 900, 400

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1
        

        key_lst = pg.key.get_pressed()
        for k, mv in delta.items():
            if key_lst[k]:
                kk_rect.move_ip((mv))  # keyに応じてこうかとんを動かす
                if cheack_bound(screen.get_rect(), kk_rect) != (True, True):
                    for k, mv in delta.items():
                        if key_lst[k]:
                            kk_rect.move_ip((-mv[0], -mv[1]))
        
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rect)
        bb_rect.move_ip(vx, vy)  #爆弾を動かす
        yoko, tate = cheack_bound(screen.get_rect(), bb_rect)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        
        screen.blit(bb_img, bb_rect)
        if kk_rect.colliderect(bb_rect):
            return

        screen.blit(bb_img, bb_rect)
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()