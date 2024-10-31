class ReadmeMaker < Formula
  desc "A CLI tool to generate structured README.md files using OpenAI API."
  homepage "https://github.com/CalebSargeant/readme-maker"
  url "https://github.com/CalebSargeant/readme-maker/archive/refs/tags/v0.1.0.tar.gz"
  sha256 "5aa1bc8f89d4326990c129ab6a94a6d6d7b2d12c1be98c3492f65b3a92fba85a"
  license "MIT"

  depends_on "python@3.9"  # Ensure Python 3.9 is installed

  def install
    # Install Python dependencies into libexec to isolate from system Python
    system "pip3", "install", "--prefix=#{libexec}", "."

    # Create a wrapper script for the `readme` command
    (bin/"readme").write_env_script libexec/"bin/readme", :PYTHONPATH => libexec/"lib/python3.9/site-packages"
  end

  test do
    # Check if the `readme` command runs successfully
    system "#{bin}/readme", "--help"
  end
end