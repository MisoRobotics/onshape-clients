/*
 * Onshape REST API
 *
 * The Onshape REST API consumed by all clients.
 *
 * API version: 1.111
 * Contact: api-support@onshape.zendesk.com
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi
// BtmParameterQueryWithOccurrenceList67AllOf struct for BtmParameterQueryWithOccurrenceList67AllOf
type BtmParameterQueryWithOccurrenceList67AllOf struct {
	Occurrences []BtOccurrence74 `json:"occurrences,omitempty"`
	Queries []BtmIndividualQueryWithOccurrenceBase904 `json:"queries,omitempty"`
	BtType string `json:"btType,omitempty"`
}
