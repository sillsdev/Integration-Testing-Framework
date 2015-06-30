#!/bin/bash
kill `pidof mono`
(fieldworks-flex &)
(sikuli ./examples/1_open_flex_existing.sikuli)

