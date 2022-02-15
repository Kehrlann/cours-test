#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"

unsigned int Increment( unsigned int number ) {
    return number + 1;
}

TEST_CASE( "increment" ) {
    REQUIRE( Increment(5) == 6 );
    REQUIRE( Increment(-5) == -4 );
}

