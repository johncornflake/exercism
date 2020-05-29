// it's a twofer, broh!
package twofer

import "fmt"

// Returns an example for how to share using a given name
// defaults to "you" if the sperson is cautious and does not tell you their name.
func ShareWith(name string) string {
    if name == "" {
        name = "you"
  }
  return fmt.Sprintf("One for %v, one for me.", name)
}
