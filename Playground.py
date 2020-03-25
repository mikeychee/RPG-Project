while not ended:
    alive = True

    print(
        "A wild " + random_creature.name + " appeared!"
    )

    print(
        "You chose " + current_creature.name + "!"
    )

    while alive:

        call = input("What would you like to do? [Run/Fight] > ")

        if call == 'fight':
            print(current_creature.move_set)

            move = input("What move would you like to choose? > ")

            if move == current_creature.move_list[0]:
                print(current_creature.name + " used " + current_creature.move_list[0])

                dmg = random_creature.take_dmg(current_creature.move_set[current_creature.move_list[0]][0],
                                               current_creature.move_set[current_creature.move_list[0]][1],
                                               random_creature.type)

                print(random_creature.name + " took " + str(dmg) + " damage!")

                print(" ")

                if random_creature.hp >= 0:
                    print(random_creature.name + " has " + str(random_creature.hp) + " hp left!")

            elif move == current_creature.move_list[1]:
                print(current_creature.name + " used " + current_creature.move_list[1])

                dmg = random_creature.take_dmg(current_creature.move_set[current_creature.move_list[1]][0],
                                               current_creature.move_set[current_creature.move_list[1]][1],
                                               random_creature.type)

                print(random_creature.name + " took " + str(dmg) + " damage!")

                print(" ")

                if random_creature.hp >= 0:
                    print(random_creature.name + " has " + str(random_creature.hp) + " hp left!")

            elif move == current_creature.move_list[2]:
                print(current_creature.name + " used " + current_creature.move_list[2])

                dmg = random_creature.take_dmg(current_creature.move_set[current_creature.move_list[2]][0],
                                               current_creature.move_set[current_creature.move_list[2]][1],
                                               random_creature.type)

                print(random_creature.name + " took " + str(dmg) + " damage!")

                print(" ")
                if random_creature.hp >= 0:
                    print(random_creature.name + " has " + str(random_creature.hp) + " hp left!")

            elif move == current_creature.move_list[3]:
                print(current_creature.name + " used " + current_creature.move_list[3])

                dmg = random_creature.take_dmg(current_creature.move_set[current_creature.move_list[3]][0],
                                               current_creature.move_set[current_creature.move_list[3]][1],
                                               random_creature.type)

                print(random_creature.name + " took " + str(dmg) + " damage!")

                print(" ")
                if random_creature.hp >= 0:
                    print(random_creature.name + " has " + str(random_creature.hp) + " hp left!")

            elif move not in current_creature.move_list:
                print("Please pick a move")

            if random_creature.hp <= 0:
                print("The wild " + random_creature.name + " fainted!")
                alive = False
                ended = True

        elif call == "run":
            random_int = random.randint(1, 3)
            if random_int == 1:
                print("Got away safely!")
                ended = True
                alive = False
            elif random_int != 1:
                print("Couldn't get away!")

#     if event.type == pygame.MOUSEBUTTONDOWN:
#         if fight_button.rect.x < mouse[0] < (
#                 fight_button.rect.x + fight_button.rect[2]):
#             if fight_button.rect.y < mouse[1] < (
#                     fight_button.rect.y + fight_button.rect[3]):
#                 # add what happens after fight button is clicked here
#                 print("click")
#
#                 self.scene.set_background(config.battle_background, self.scene_surface)
#                 self.play_scene()
#
#                 move1B.draw()
#                 move2B.draw()
#                 move3B.draw()
#                 move4B.draw()
#
#                 move1T.draw_text()
#                 move2T.draw_text()
#                 move3T.draw_text()
#                 move4T.draw_text()
#
#                 self.screen.blit(move1S, (163, 352))
#                 self.screen.blit(move2S, (320, 352))
#                 self.screen.blit(move3S, (163, 414))
#                 self.screen.blit(move4S, (320, 414))
#
#                 print(event)
#                 count = -1
#
#         if run_button.rect.x < mouse[0] < (
#                 run_button.rect.x + run_button.rect[2]):
#             if run_button.rect.y < mouse[1] < (
#                     run_button.rect.y + run_button.rect[3]):
#                 # add what happens after run button is clicked here
#                 print("click")
#                 random_int = random.randint(1, 2)
#                 if random_int == 1:
#                     print("Got away safely!")
#                     self.scene.set_background(config.battle_background, self.scene_surface)
#                     success_esc.draw_text()
#                     self.play_scene()
#
#                     count = 5
#                     alive = False
#
#                 elif random_int != 1:
#                     print("Couldn't get away!")
#                     self.scene.set_background(config.battle_background, self.scene_surface)
#                     failed_esc.draw_text()
#                     self.play_scene()
#                     count = 1
#
#                     self.play_scene()
#
#                     alive = False
#
#     elif event.type == pygame.MOUSEMOTION:
#         if fight_button.rect.x < mouse[0] < (
#                 fight_button.rect.x + fight_button.rect[2]):
#             if fight_button.rect.y < mouse[1] < (
#                     fight_button.rect.y + fight_button.rect[3]):
#                 # print("hover")
#                 fight_button.image = config.fight_button_H
#                 fight_button.draw()
#
#             else:
#                 fight_button.image = config.fight_button
#                 fight_button.draw()
#
#         if run_button.rect.x < mouse[0] < (
#                 run_button.rect.x + run_button.rect[2]):
#             if run_button.rect.y < mouse[1] < (
#                     run_button.rect.y + run_button.rect[3]):
#                 # print("hover")
#                 run_button.image = config.run_button_H
#                 run_button.draw()
#
#             else:
#                 run_button.image = config.run_button
#                 run_button.draw()
#
#     elif event.type == pygame.KEYDOWN:
#
#         if event.key == pygame.K_ESCAPE:
#             quit()
#
# if count == -1:  # attack selections
#     pygame.event.clear()
#
#     if event.type == pygame.MOUSEBUTTONDOWN and count == -1:
#
#         if 163 < mouse[0] < (
#                 163 + move1S.get_rect()[2]):
#             if 352 < mouse[1] < (
#                     352 + move1S.get_rect()[3]):
#                 print("Move 1")
#
#         if 320 < mouse[0] < (
#                 320 + move2S.get_rect()[2]):
#             if 352 < mouse[1] < (
#                     352 + move2S.get_rect()[3]):
#                 print("Move 2")
#
#         if 163 < mouse[0] < (
#                 163 + move3S.get_rect()[2]):
#             if 414 < mouse[1] < (
#                     414 + move3S.get_rect()[3]):
#                 print("Move 3")
#
#         if 320 < mouse[0] < (
#                 320 + move4S.get_rect()[2]):
#             if 414 < mouse[1] < (
#                     414 + move4S.get_rect()[3]):
#                 print("Move 4")
#
#     elif event.type == pygame.MOUSEMOTION:
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if back.rect.x < mouse[0] < (
#                     back.rect.x + back.rect[2]):
#                 if back.rect.y < mouse[1] < (
#                         back.rect.y + back.rect[3]):
#                     pass
#
#     elif event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_b:
#             count = 2
#
#             if count < len(battle_texts):
#                 self.scene.set_background(config.battle_background, self.scene_surface)
#
#                 battle_texts[count].draw_text()
#                 self.play_scene()
#
#                 if count == 2:
#                     fight_button.draw()
#                     run_button.draw()
#                     print("draw buttons")