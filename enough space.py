def enough(cap, on, wait):

    total_num_passenger= on + wait
    if total_num_passenger > cap:
         return  total_num_passenger - cap
    else:
        return 0

