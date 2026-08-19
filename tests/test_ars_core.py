"""Tests for ARSKernel - Adaptive Recursive System core logic."""
import pytest
from user.arsd.ars_core import ARSKernel


class TestARSKernelInit:
    """Test ARSKernel initialization."""

    def test_init_defaults(self):
        """Test ARSKernel initializes with correct default values."""
        kernel = ARSKernel()
        assert kernel.prev == 0
        assert kernel.curr == 1
        assert kernel.history == []

    def test_init_history_empty(self):
        """Test history starts empty."""
        kernel = ARSKernel()
        assert isinstance(kernel.history, list)
        assert len(kernel.history) == 0


class TestARSKernelAdapt:
    """Test ARSKernel.adapt() method."""

    def test_adapt_basic_sequence(self):
        """Test adapt produces Fibonacci-like sequence without context."""
        kernel = ARSKernel()
        # prev=0, curr=1: nxt = 1 + (1-0) + 0 = 2
        assert kernel.adapt(0) == 2
        # prev=1, curr=2: nxt = 2 + (2-1) + 0 = 3
        assert kernel.adapt(0) == 3
        # prev=2, curr=3: nxt = 3 + (3-2) + 0 = 4
        assert kernel.adapt(0) == 4

    def test_adapt_updates_prev_curr(self):
        """Test adapt correctly updates prev and curr."""
        kernel = ARSKernel()
        kernel.adapt(0)
        assert kernel.prev == 1
        assert kernel.curr == 2

        kernel.adapt(0)
        assert kernel.prev == 2
        assert kernel.curr == 3

    def test_adapt_with_context(self):
        """Test adapt incorporates context parameter."""
        kernel = ARSKernel()
        # prev=0, curr=1: nxt = 1 + (1-0) + 5 = 7
        result = kernel.adapt(context=5)
        assert result == 7
        assert kernel.curr == 7

    def test_adapt_records_history(self):
        """Test adapt records each result in history."""
        kernel = ARSKernel()
        kernel.adapt(0)
        kernel.adapt(0)
        kernel.adapt(0)
        assert kernel.history == [2, 3, 4]

    def test_adapt_negative_context(self):
        """Test adapt handles negative context."""
        kernel = ARSKernel()
        # prev=0, curr=1: nxt = 1 + (1-0) - 2 = 0
        result = kernel.adapt(context=-2)
        assert result == 0

    def test_adapt_large_context(self):
        """Test adapt handles large context values."""
        kernel = ARSKernel()
        result = kernel.adapt(context=1000)
        assert result == 1002  # 1 + 1 + 1000


class TestARSKernelRunSteps:
    """Test ARSKernel.run_steps() method."""

    def test_run_steps_default(self):
        """Test run_steps with default parameters."""
        kernel = ARSKernel()
        results = kernel.run_steps(steps=3)
        assert len(results) == 3
        assert results == [2, 3, 4]

    def test_run_steps_single_step(self):
        """Test run_steps with single step."""
        kernel = ARSKernel()
        results = kernel.run_steps(steps=1)
        assert results == [2]

    def test_run_steps_updates_history(self):
        """Test run_steps records all results in history."""
        kernel = ARSKernel()
        kernel.run_steps(steps=5)
        assert len(kernel.history) == 5
        assert kernel.history == [2, 3, 4, 5, 6]

    def test_run_steps_with_context_function(self):
        """Test run_steps with custom context function."""
        kernel = ARSKernel()

        def context_fn(i):
            return i * 10

        results = kernel.run_steps(steps=3, context_fn=context_fn)
        # Step 0: 1 + 1 + 0 = 2
        # Step 1: 2 + 1 + 10 = 13
        # Step 2: 13 + 11 + 20 = 44
        assert results == [2, 13, 44]

    def test_run_steps_context_function_receives_index(self):
        """Test that context function receives correct step index."""
        kernel = ARSKernel()
        indices_seen = []

        def context_fn(i):
            indices_seen.append(i)
            return 0

        kernel.run_steps(steps=4, context_fn=context_fn)
        assert indices_seen == [0, 1, 2, 3]

    def test_run_steps_zero_steps(self):
        """Test run_steps with zero steps."""
        kernel = ARSKernel()
        results = kernel.run_steps(steps=0)
        assert results == []
        assert kernel.history == []

    def test_run_steps_maintains_state(self):
        """Test run_steps maintains kernel state between calls."""
        kernel = ARSKernel()
        kernel.run_steps(steps=2)
        assert kernel.curr == 3
        assert kernel.prev == 2

        # Continue from where we left off
        kernel.run_steps(steps=2)
        assert kernel.history == [2, 3, 4, 5]

    def test_run_steps_large_context(self):
        """Test run_steps with large context values."""
        kernel = ARSKernel()

        def context_fn(i):
            return 100 + i

        results = kernel.run_steps(steps=2, context_fn=context_fn)
        # Step 0: 1 + 1 + 100 = 102
        # Step 1: 102 + 101 + 101 = 304
        assert results == [102, 304]


class TestARSKernelIntegration:
    """Integration tests for ARSKernel."""

    def test_multiple_kernel_instances_independent(self):
        """Test multiple kernel instances don't share state."""
        kernel1 = ARSKernel()
        kernel2 = ARSKernel()

        kernel1.run_steps(steps=2)
        kernel2.run_steps(steps=3)

        assert kernel1.history == [2, 3]
        assert kernel2.history == [2, 3, 4]

    def test_adapt_then_run_steps(self):
        """Test calling adapt and run_steps in sequence."""
        kernel = ARSKernel()
        kernel.adapt(0)
        assert kernel.curr == 2

        results = kernel.run_steps(steps=2)
        # After adapt(0), prev=1, curr=2
        # Step 0: 2 + 1 = 3
        # Step 1: 3 + 1 = 4
        assert results == [3, 4]
        assert kernel.history == [2, 3, 4]
