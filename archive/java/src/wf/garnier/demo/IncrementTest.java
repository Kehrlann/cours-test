package wf.garnier.demo;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class IncrementTest {

    @Test
    public void increment() {
        assertEquals(Increment.increment(5), 6);
        assertEquals(Increment.increment(-5), -4);
    }
}