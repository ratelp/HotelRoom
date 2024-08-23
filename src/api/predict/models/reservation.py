class Reservation:
    def __init__(self, **args):
         # Inicializa todos os atributos de acordo com os dados fornecidos
         # Caso algum dado não esteja presente, o valor padrão de 0 é aplicado para evitar erros
         self.no_of_adults = args.get('no_of_adults',  0)
         self.no_of_children = args.get('no_of_children',  0)
         self.no_of_weekend_nights = args.get('no_of_weekend_nights',  0)
         self.no_of_week_nights = args.get('no_of_week_nights',  0)
         self.required_car_parking_space = args.get('required_car_parking_space',  0)
         self.lead_time = args.get('lead_time',  0)
         self.arrival_year = args.get('arrival_year',  0)
         self.arrival_month = args.get('arrival_month',  0)
         self.arrival_date = args.get('arrival_date',  0)
         self.repeated_guest = args.get('repeated_guest',  0)
         self.no_of_previous_cancellations = args.get('no_of_previous_cancellations',  0)
         self.no_of_previous_bookings_not_canceled = args.get('no_of_previous_bookings_not_canceled',  0)
         self.no_of_special_requests = args.get('no_of_special_requests',  0)
         (self.type_of_meal_plan_1, self.type_of_meal_plan_2, self.type_of_meal_plan_3, self.type_of_meal_plan_4) = self._get_type_of_meal_plan(args['type_of_meal_plan']) if 'type_of_meal_plan' in args else (0, 0, 0, 0)
         (self.room_type_1, self.room_type_2, self.room_type_3, self.room_type_4, self.room_type_5, self.room_type_6, self.room_type_7) = self._get_room_type_reserved(args['room_type_reserved']) if 'room_type_reserved' in args else (0, 0, 0, 0, 0, 0, 0)
         (self.market_1, self.market_2, self.market_3, self.market_4, self.market_5) = self._get_market(args['market_segment_type']) if 'market_segment_type' in args else (0, 0, 0, 0, 0)
         (self.booking_status_1, self.booking_status_2) = self._get_booking_status(args['booking_status']) if 'booking_status' in args else (0, 0)


    def _get_type_of_meal_plan(self, meal_plan):
        # Pega o último caractere de "type_of_meal_plan" para determinar o tipo
        mp = meal_plan[-1]

        if not str.isnumeric(mp):
            if mp != 'd':
                # Valor inválido
                raise ValueError
            
            # Se o último caractere não for um dígito, é "Not_Selected"
            mp = 4

        response = [0] * 4
        response[int(mp) - 1] = 1

        return response
    

    def _get_room_type_reserved(self, rtr):
        # Pega o último caractere de "room_type_reserved" para determinar o tipo
        rtr = rtr[-1]

        if not str.isnumeric(rtr):
            # Valor inválido
            raise ValueError

        response = [0] * 7
        response[int(rtr) - 1] = 1

        return response

    def _get_market(self, mkt):
        responses = {
            "Aviation": 0,
            "Complementary": 1,
            "Corporate": 2,
            "Offline": 3,
            "Online": 4,
        }

        if mkt not in responses.keys():
            # Valor Inválido
            raise ValueError

        response = [0] * 5

        response[responses[mkt]] = 1

        return response
    
    def _get_booking_status(self, bs):
        responses = {
            "Canceled": 0,
            "Not_Canceled": 1,
        }

        if bs not in responses.keys():
            # Valor Inválido
            raise ValueError

        response = [0] * 2
        response[responses[bs]] = 1

        return response