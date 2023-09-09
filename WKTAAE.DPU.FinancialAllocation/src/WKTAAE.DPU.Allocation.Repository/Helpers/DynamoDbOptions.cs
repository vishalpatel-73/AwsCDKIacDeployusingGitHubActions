
namespace WKTAAE.DPU.Allocation.Repository.Helpers
{
    public class DynamoDbOptions
    {
        public string Region { get; set; }

        public string AccessKey { get; set; }

        public string SecretKey { get; set; }

        public string LocalhostUrl { get; set; }

        public string DocumentTablePrefix { get; set; }
    }
}
