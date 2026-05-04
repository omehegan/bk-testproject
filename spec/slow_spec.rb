# This file is intentionally slow to test split_by_example.
# It should be flagged as a "slow file" by Test Engine and split into examples.
RSpec.describe "SlowTests" do
  it "test 1 (slow)" do
    sleep 10
    expect(true).to be true
  end

  it "test 2 (slow)" do
    sleep 10
    expect(true).to be true
  end

  it "test 3 (slow)" do
    sleep 10
    expect(true).to be true
  end
end
