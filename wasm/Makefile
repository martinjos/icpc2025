PKGS := python3-embed
CFLAGS := `pkg-config --cflags $(PKGS)`
LDLIBS := `pkg-config --libs $(PKGS)`
CPPFLAGS := -MMD
CFLAGS += -g

TARGETS := test_insert

all: $(TARGETS)

clean:
	-$(RM) *.o *.d bridge.c $(TARGETS)

test_insert: test_insert.o bridge.o

%: %.o bridge.o
	$(CC) $(LDFLAGS) $(CFLAGS) -o $@ $^ $(LDLIBS)

%.c: %.pyx
	cython -3 $<

.SECONDARY:  # Don't delete intermediate files

sinclude *.d