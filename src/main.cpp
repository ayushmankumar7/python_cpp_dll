#include <iostream>
#include "inlcudes/example.hpp"

extern "C"{
    __declspec(dllexport) int print_loop(int a){
        for(int i = 0; i < a; i++){
            // std::cout << i << '\n';
            printf("%d\n", i);
        }
        return 0;
    }
}