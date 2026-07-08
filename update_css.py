with open(r"d:\Portfolio\css\styles.css", "a") as f:
    f.write("""

/* Hero Diagram Layout */
.hero-diagram-wrapper {
  position: relative;
  height: 100%;
  margin-top: var(--spacing-8);
}
.hero-diagram-svg {
  width: 100%;
  height: auto;
  padding: 20px 0;
}
@media (min-width: 768px) {
  .hero-diagram-wrapper {
    margin-top: 150px;
  }
}
@media (min-width: 1024px) {
  .hero-diagram-wrapper {
    margin-top: 220px;
  }
}
""")
