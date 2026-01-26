# CppUTest

- CppUTest notes

## Index

- [CppUMock API](#cppumock-api)
- [CppUTest API](#cpputest-api)

## CppUMock API

```
================================================================================
Setup and teardown

TEST_GROUP(RepeatHelloWorldTests)
{
    void setup() override
    {
        mock().clear();
    }

    void teardown() override
    {
        mock().checkExpectations();
        mock().clear();
    }
};

================================================================================
Declaring expectations

TEST(RepeatHelloWorldTests, ShouldCallPrintTwice)
{
    mock().expectNCalls(2, "printHelloWorld");
    printHelloWorldTwice();
}

mock().expectOneCall("gpio_write")
mock().expectNCalls(2, "printHelloWorld")
mock().expectNoCall("hardware_reset")

================================================================================
Matching arguments

- Integer arguments
mock().expectOneCall("gpio_set")
      .withIntParameter("pin", 5)
      .withIntParameter("value", 1);

- Unsigned / long / pointer
.withUnsignedIntParameter("mask", 0xFF)
.withLongIntParameter("count", 10)
.withPointerParameter("buffer", buf);

- String parameter
.withStringParameter("name", "UART1");

- Memory buffers
.withMemoryBufferParameter("data", expected, size);

================================================================================
Returning values

- Return integer
mock().expectOneCall("adc_read")
      .andReturnValue(123);

- Return pointer
mock().expectOneCall("malloc")
      .andReturnValue(ptr);

- Return boolean
.andReturnValue(true);

================================================================================
Output parameters

mock().expectOneCall("adc_read")
      .withIntParameter("channel", 3)
      .withOutputParameterReturning(
          "value", &fakeValue, sizeof(fakeValue));

================================================================================
Call order enforcement

mock().strictOrder();

================================================================================
Defining mocked functions

extern "C" void printHelloWorld(void)
{
    mock().actualCall("printHelloWorld");
}

int gpio_read(int pin)
{
    return mock()
        .actualCall("gpio_read")
        .withIntParameter("pin", pin)
        .returnIntValue();
}

void gpio_write(int pin, int value)
{
    mock()
        .actualCall("gpio_write")
        .withIntParameter("pin", pin)
        .withIntParameter("value", value);
}

```

## CppUTest API

- Test Structure & Registration
  - Define a test fixture
    - `TEST_GROUP(group_name)`
    - `setup()` and `teardown()` are called before and after each test
  - Define a test case
    - `TEST(group_name, test_name)`
  - Temporarily disable the test
    - `IGNORE_TEST(group_name, test_name)`
- Assertions
  - General conditional check
    - `CHECK(condition)`, `CHECK_FALSE(condition)`
  - Integer equality (int, uint8_t, uint32_t, enums, etc)
    - `CHECK_EQUAL(expected, actual)`
  - Long equality
    - `LONGS_EQUAL(expected, actual)`
    - ...int32_t on weird platforms
  - Hex value checking
    - `CHECK_EQUAL_HEX(expected, actual)`
    - Useful for registers
  - Floating point checking
    - `DOUBLES_EQUAL(expected, actual, tolerance)`
  - Pointer checking
    - `POINTERS_EQUAL(expected, actual)`
  - String value checking
    - `STRCMP_EQUAL(expected, actual)`, `STRNCMP_EQUAL(expected, actual, length)`
  - Memory block checking
    - `MEMCMP_EQUAL(expected, actual, size)`
  - Null checking
    - `CHECK_NULL(ptr)`, `CHECK_NOT_NULL(ptr)`
  - Explicit failure
    - `FAIL("Should not reach here")`
