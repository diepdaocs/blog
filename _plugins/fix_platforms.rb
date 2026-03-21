# Patch for Jekyll 3.9 + Ruby 3.1: pathutil's read() signature changed,
# breaking proc_version which is used by the file watcher.
module Jekyll
  module Utils
    module Platforms
      def proc_version
        ""
      end
    end
  end
end
