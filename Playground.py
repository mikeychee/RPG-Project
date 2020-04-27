def game_mechanics(self):
    global dmg
    print("set up battle scene")
    # setting up the variables for the game
    sequence_texts = []
    battle_texts = []

    ended = False
    current_creature = self.my_creatures[0]
    random_creature = self.route1[random.randint(0, len(self.route1) - 1)]
    random_creature.hp = random_creature.max_hp

    starting_text = Text_Controller(self.scene_surface, "A wild " + random_creature.name + " appeared!",
                                    config.game_messages, (15, 380), config.black)
    chosen_text = Text_Controller(self.scene_surface, "You chose " + current_creature.name + "!",
                                  config.game_messages, (15, 380), config.black)
    call_text = Text_Controller(self.scene_surface, "What would you like to do?", config.game_messages_small,
                                (15, 360), config.black)
    failed_esc = Text_Controller(self.scene_surface, "Couldn't get away!", config.game_messages,
                                 (15, 360), config.black)
    success_esc = Text_Controller(self.scene_surface, "Got away safely!", config.game_messages,
                                  (15, 360), config.black)

    sequence_texts.append(starting_text)
    sequence_texts.append(chosen_text)  # this order is important as it is the order in which the messages
    sequence_texts.append(call_text)  # are played

    fight_button = Button(self.screen, config.fight_button, (150, 400))
    run_button = Button(self.screen, config.run_button, (350, 400))

    move1S = pygame.Surface((154, 60))
    move2S = pygame.Surface((154, 60))
    move3S = pygame.Surface((154, 60))
    move4S = pygame.Surface((154, 60))

    self.screen.blit(move1S, (6, 352))
    self.screen.blit(move2S, (163, 352))
    self.screen.blit(move3S, (320, 352))
    self.screen.blit(move4S, (477, 352))

    move1B = Button(move1S, config.button_template, (0, 0))
    move2B = Button(move2S, config.button_template, (0, 0))
    move3B = Button(move3S, config.button_template, (0, 0))
    move4B = Button(move4S, config.button_template, (0, 0))

    back = Button(self.screen, config.button_template, (243, 414))
    backT = Text_Controller(self.screen, "Back", config.game_messages, (285, 429), config.black)

    move1T = Text_Controller(move1S, current_creature.move_list[0], config.game_messages_small, (10, 20),
                             config.black)
    move2T = Text_Controller(move2S, current_creature.move_list[1], config.game_messages_small, (10, 20),
                             config.black)
    move3T = Text_Controller(move3S, current_creature.move_list[2], config.game_messages_small, (10, 20),
                             config.black)
    move4T = Text_Controller(move4S, current_creature.move_list[3], config.game_messages_small, (10, 20),
                             config.black)

    chosen_move1 = Text_Controller(self.scene_surface,
                                   current_creature.name + " used "
                                   + current_creature.move_list[0] + " !",
                                   config.game_messages,
                                   (15, 360), config.black)
    chosen_move2 = Text_Controller(self.scene_surface,
                                   current_creature.name + " used "
                                   + current_creature.move_list[1] + " !",
                                   config.game_messages,
                                   (15, 360), config.black)
    chosen_move3 = Text_Controller(self.scene_surface,
                                   current_creature.name + " used "
                                   + current_creature.move_list[2] + " !",
                                   config.game_messages,
                                   (15, 360), config.black)
    chosen_move4 = Text_Controller(self.scene_surface,
                                   current_creature.name + " used "
                                   + current_creature.move_list[3] + " !",
                                   config.game_messages,
                                   (15, 360), config.black)

    creature_health_text = Text_Controller(self.scene_surface,
                                           random_creature.name + " has " + str(random_creature.hp) + " hp left!",
                                           config.game_messages,
                                           (15, 360), config.black)

    fainted_text = Text_Controller(self.scene_surface,
                                   random_creature.name + " fainted!", config.game_messages,
                                   (15, 360), config.black)

    super_effective_text = Text_Controller(self.scene_surface,
                                           "It's super effective!", config.game_messages,
                                           (15, 360), config.black)

    not_effective_text = Text_Controller(self.scene_surface,
                                         "It's not very effective", config.game_messages,
                                         (15, 360), config.black)

    sequence_texts[0].draw_text()
    self.play_scene()
    count = 0
    battle_count = 0

    selections = [fight_button, run_button]
    alive = False
    bool = True

    current_selection = 0
    # game code
    while not ended:
        # TODO: Health bars
        # draw a rect that uses the health bar percentage as the width
        # so that when the health goes down, the bar will be shorter as the rect width would be shorter
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                quit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    print(random_creature.hp)

                    if not alive:
                        count += 1

                    if 0 < count < len(sequence_texts):
                        self.scene.set_background(config.battle_background, self.scene_surface)

                        sequence_texts[count].draw_text()
                        self.play_scene()

                        if count == 2:

                            selections = [fight_button, run_button]

                            fight_button.draw()
                            run_button.draw()
                            print("draw buttons")

                            alive = True
                            battle_count = 0

                            if current_selection == 0:
                                selections[0].image = config.fight_button_H
                                selections[0].draw()
                            elif current_selection == 1:
                                selections[1].image = config.run_button_H
                                selections[1].draw()

                if event.key == pygame.K_ESCAPE:
                    quit()

            if count == 2 and battle_count == 0:
                selections = [fight_button, run_button]
                current_selection = 0

                if event.type == pygame.KEYUP:

                    if event.key == pygame.K_d:
                        current_selection += 1

                    elif event.key == pygame.K_a:
                        current_selection -= 1

                    if current_selection > len(selections) - 1:
                        current_selection = len(selections) - 1
                    elif current_selection < 0:
                        current_selection = 0

                    if current_selection == 0 and count != -1:
                        selections[0].image = config.fight_button_H
                        selections[1].image = config.run_button
                        selections[0].draw()
                        selections[1].draw()

                        if event.key == pygame.K_c:
                            print("select fight")

                            self.scene.set_background(config.battle_background, self.scene_surface)
                            self.play_scene()

                            move1B.image = config.button_template
                            move2B.image = config.button_template
                            move3B.image = config.button_template
                            move4B.image = config.button_template

                            move1B.draw()
                            move2B.draw()
                            move3B.draw()
                            move4B.draw()

                            move1T.draw_text()
                            move2T.draw_text()
                            move3T.draw_text()
                            move4T.draw_text()

                            self.screen.blit(move1S, (163, 352))
                            self.screen.blit(move2S, (320, 352))
                            self.screen.blit(move3S, (163, 414))
                            self.screen.blit(move4S, (320, 414))

                            count = -1

                    elif current_selection == 1:
                        selections[1].image = config.run_button_H
                        selections[0].image = config.fight_button
                        selections[1].draw()
                        selections[0].draw()

                        if event.key == pygame.K_c:
                            print("select run")

                            random_int = random.randint(1, 2)
                            if random_int == 1:
                                print("Got away safely!")
                                self.scene.set_background(config.battle_background, self.scene_surface)
                                success_esc.draw_text()
                                self.play_scene()

                                count = 5
                                alive = False

                            elif random_int != 1:
                                print("Couldn't get away!")
                                self.scene.set_background(config.battle_background, self.scene_surface)
                                failed_esc.draw_text()
                                self.play_scene()
                                count = 1

                                self.play_scene()

                                alive = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    count = 2

                    if count < len(sequence_texts):
                        self.scene.set_background(config.battle_background, self.scene_surface)

                        sequence_texts[count].draw_text()
                        self.play_scene()

                        if count == 2:
                            fight_button.draw()
                            run_button.draw()
                            print("draw buttons")

            if count == -1:
                alive = True
                selections = [move1B, move2B, move3B, move4B]
                battle_texts = []

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        current_selection += 1

                    elif event.key == pygame.K_a:
                        current_selection -= 1

                    elif 0 <= current_selection <= 1 and event.key == pygame.K_s:
                        current_selection += 2

                    elif 2 <= current_selection <= 3 and event.key == pygame.K_w:
                        current_selection -= 2

                    if current_selection > len(selections) - 1:
                        current_selection = len(selections) - 1
                    elif current_selection < 0:
                        current_selection = 0

                    if current_selection == 0:
                        selections[0].image = config.button_template_H
                        selections[1].image = config.button_template
                        selections[2].image = config.button_template
                        selections[3].image = config.button_template

                        selections[0].draw()
                        selections[1].draw()
                        selections[2].draw()
                        selections[3].draw()

                        move1T.draw_text()
                        move2T.draw_text()
                        move3T.draw_text()
                        move4T.draw_text()

                        self.screen.blit(move1S, (163, 352))
                        self.screen.blit(move2S, (320, 352))
                        self.screen.blit(move3S, (163, 414))
                        self.screen.blit(move4S, (320, 414))

                        if event.key == pygame.K_c:
                            # first selection

                            battle_count = 0
                            print(current_creature.name + " used " + current_creature.move_list[0] + " !")
                            battle_texts.append(chosen_move1)

                            dmg = random_creature.take_dmg(
                                current_creature.move_set[current_creature.move_list[0]][0],
                                current_creature.move_set[current_creature.move_list[0]][1],
                                random_creature.type)

                            take_dmg_text = Text_Controller(self.scene_surface,
                                                            random_creature.name + " took " + str(dmg) + " damage!",
                                                            config.game_messages, (15, 360), config.black)
                            effectiveness = random_creature.get_effectiveness(current_creature.move_set
                                                                              [current_creature.move_list[0]][1],
                                                                              random_creature.type)

                            if effectiveness == 1:
                                battle_texts.append(super_effective_text)

                            elif effectiveness == 2:
                                battle_texts.append(not_effective_text)

                            creature_health_text = Text_Controller(self.scene_surface,
                                                                   random_creature.name + " has " + str(
                                                                       random_creature.hp) + " hp left!",
                                                                   config.game_messages,
                                                                   (15, 360), config.black)

                            battle_texts.append(take_dmg_text)
                            battle_texts.append(creature_health_text)
                            battle_texts[0].draw_text()

                            battle_texts[0].draw_text()
                            self.play_scene()

                            count = -2

                    elif current_selection == 1:
                        selections[0].image = config.button_template
                        selections[1].image = config.button_template_H
                        selections[2].image = config.button_template
                        selections[3].image = config.button_template

                        selections[0].draw()
                        selections[1].draw()
                        selections[2].draw()
                        selections[3].draw()

                        move1T.draw_text()
                        move2T.draw_text()
                        move3T.draw_text()
                        move4T.draw_text()

                        self.screen.blit(move1S, (163, 352))
                        self.screen.blit(move2S, (320, 352))
                        self.screen.blit(move3S, (163, 414))
                        self.screen.blit(move4S, (320, 414))

                        if event.key == pygame.K_c:
                            # second selection

                            battle_count = 0
                            print(current_creature.name + " used " + current_creature.move_list[1] + " !")
                            battle_texts.append(chosen_move2)

                            dmg = random_creature.take_dmg(
                                current_creature.move_set[current_creature.move_list[1]][0],
                                current_creature.move_set[current_creature.move_list[1]][1],
                                random_creature.type)

                            take_dmg_text = Text_Controller(self.scene_surface,
                                                            random_creature.name + " took " + str(dmg) + " damage!",
                                                            config.game_messages, (15, 360), config.black)
                            effectiveness = random_creature.get_effectiveness(current_creature.move_set
                                                                              [current_creature.move_list[1]][1],
                                                                              random_creature.type)

                            if effectiveness == 1:
                                battle_texts.append(super_effective_text)
                            elif effectiveness == 2:
                                battle_texts.append(not_effective_text)

                            creature_health_text = Text_Controller(self.scene_surface,
                                                                   random_creature.name + " has " + str(
                                                                       random_creature.hp) + " hp left!",
                                                                   config.game_messages,
                                                                   (15, 360), config.black)

                            battle_texts.append(take_dmg_text)
                            battle_texts.append(creature_health_text)
                            battle_texts[0].draw_text()

                            battle_texts[0].draw_text()
                            self.play_scene()

                            count = -2

                    elif current_selection == 2:
                        selections[0].image = config.button_template
                        selections[1].image = config.button_template
                        selections[2].image = config.button_template_H
                        selections[3].image = config.button_template

                        selections[0].draw()
                        selections[1].draw()
                        selections[2].draw()
                        selections[3].draw()

                        move1T.draw_text()
                        move2T.draw_text()
                        move3T.draw_text()
                        move4T.draw_text()

                        self.screen.blit(move1S, (163, 352))
                        self.screen.blit(move2S, (320, 352))
                        self.screen.blit(move3S, (163, 414))
                        self.screen.blit(move4S, (320, 414))

                        if event.key == pygame.K_c:
                            # third selection

                            battle_count = 0

                            print(current_creature.name + " used " + current_creature.move_list[2] + " !")
                            battle_texts.append(chosen_move3)

                            dmg = random_creature.take_dmg(
                                current_creature.move_set[current_creature.move_list[2]][0],
                                current_creature.move_set[current_creature.move_list[2]][1],
                                random_creature.type)

                            take_dmg_text = Text_Controller(self.scene_surface,
                                                            random_creature.name + " took " + str(dmg) + " damage!",
                                                            config.game_messages, (15, 360), config.black)
                            effectiveness = random_creature.get_effectiveness(current_creature.move_set
                                                                              [current_creature.move_list[2]][1],
                                                                              random_creature.type)

                            if effectiveness == 1:
                                battle_texts.append(super_effective_text)
                            elif effectiveness == 2:
                                battle_texts.append(not_effective_text)

                            creature_health_text = Text_Controller(self.scene_surface,
                                                                   random_creature.name + " has " + str(
                                                                       random_creature.hp) + " hp left!",
                                                                   config.game_messages,
                                                                   (15, 360), config.black)

                            battle_texts.append(take_dmg_text)
                            battle_texts.append(creature_health_text)
                            battle_texts[0].draw_text()

                            battle_texts[0].draw_text()
                            self.play_scene()

                            count = -2

                elif current_selection == 3:
                    selections[0].image = config.button_template
                    selections[1].image = config.button_template
                    selections[2].image = config.button_template
                    selections[3].image = config.button_template_H

                    selections[0].draw()
                    selections[1].draw()
                    selections[2].draw()
                    selections[3].draw()

                    move1T.draw_text()
                    move2T.draw_text()
                    move3T.draw_text()
                    move4T.draw_text()

                    self.screen.blit(move1S, (163, 352))
                    self.screen.blit(move2S, (320, 352))
                    self.screen.blit(move3S, (163, 414))
                    self.screen.blit(move4S, (320, 414))

                    if event.key == pygame.K_c:
                        # fourth selection

                        battle_count = 0

                        print(current_creature.name + " used " + current_creature.move_list[3] + " !")
                        battle_texts.append(chosen_move4)

                        dmg = random_creature.take_dmg(
                            current_creature.move_set[current_creature.move_list[3]][0],
                            current_creature.move_set[current_creature.move_list[3]][1],
                            random_creature.type)
                        effectiveness = random_creature.get_effectiveness(current_creature.move_set
                                                                          [current_creature.move_list[3]][1],
                                                                          random_creature.type)

                        if effectiveness == 1:
                            battle_texts.append(super_effective_text)

                        elif effectiveness == 2:
                            battle_texts.append(not_effective_text)

                        take_dmg_text = Text_Controller(self.scene_surface,
                                                        random_creature.name + " took " + str(dmg) + " damage!",
                                                        config.game_messages, (15, 360), config.black)

                        creature_health_text = Text_Controller(self.scene_surface,
                                                               random_creature.name + " has " + str(
                                                                   random_creature.hp) + " hp left!",
                                                               config.game_messages,
                                                               (15, 360), config.black)

                        battle_texts.append(take_dmg_text)
                        battle_texts.append(creature_health_text)
                        battle_texts[0].draw_text()

                        battle_texts[0].draw_text()
                        self.play_scene()

                        count = -2

            if count == -2:
                self.scene.set_background(config.battle_background, self.scene_surface)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:

                        battle_count += 1
                        print(dmg)

                        if 0 < battle_count < len(battle_texts) and random_creature.hp > 0:
                            battle_texts[battle_count].draw_text()

                            self.play_scene()
                            print(random_creature.name + " took " + str(dmg) + " damage!")

                        if random_creature.hp <= 0:
                            fainted_text.draw_text()
                            self.play_scene()
                            count = 5
                            alive = False

                        if battle_count >= len(battle_texts) - 1:
                            count = 2
                            current_selection = 0

                        elif battle_count < 0:
                            battle_count = 0

            if count == 6:  # end sequence
                ended = True

        pygame.display.flip()

        if ended:
            self.scene.set_background(config.battle_background, self.scene_surface)
            self.game_state = Game_States.running
